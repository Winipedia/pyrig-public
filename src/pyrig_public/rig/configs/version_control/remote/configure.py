"""Shell script that applies repository configuration via the GitHub CLI."""

from pyrig.rig.configs.version_control.remote.configure import (
    ConfigureRepositoryConfigFile as BaseConfigureRepositoryConfigFile,
)
from pyrig.rig.tools.version_control.remote.controller import RemoteVersionController

from pyrig_public.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class ConfigureRepositoryConfigFile(BaseConfigureRepositoryConfigFile):
    """Add public-repository settings to the GitHub setup script.

    The additional script functions require maintainer approval for
    external contributors' pull request workflows and enable private
    vulnerability reporting.
    """

    def scripts(self) -> tuple[str, ...]:
        """Return base scripts and the public-repository policy scripts.

        Returns:
            The inherited scripts followed by fork-approval and
            vulnerability-reporting functions.
        """
        return (
            *super().scripts(),
            self.fork_pr_contributor_approval_script(),
            self.vulnerability_reporting_script(),
        )

    def fork_pr_contributor_approval_script(self) -> str:
        """Return the `fork_pr_contributor_approval` shell function.

        Returns:
            Function definition that pipes the
            `fork_pr_contributor_approval` key of the settings file into
            `gh api` as a `PUT` request.
        """
        settings_path = RepositorySettingsConfigFile.I.path().as_posix()
        key = RepositorySettingsConfigFile.I.fork_pr_contributor_approval_key()
        endpoint = (
            f'"repos/${{{self.repo_variable()}}}'
            '/actions/permissions/fork-pr-contributor-approval"'
        )
        api_call = RemoteVersionController.I.api_method_input_args(
            endpoint=endpoint,
            method="PUT",
            input_="-",
        )
        return f"""{self.fork_pr_contributor_approval_function()}() {{
  jq '.{key}' {settings_path} | {api_call}
}}"""

    def fork_pr_contributor_approval_function(self) -> str:
        """Return `RepositorySettingsConfigFile.I.fork_pr_contributor_approval_key()`.

        Named identically to the settings file key it reads, so both stay
        in sync automatically.
        """
        return RepositorySettingsConfigFile.I.fork_pr_contributor_approval_key()

    def vulnerability_reporting_script(self) -> str:
        """Return the `vulnerability_reporting` shell function.

        Returns:
            Function definition that `PUT`s the GitHub API endpoint that
            enables private vulnerability reporting for the repository.
        """
        endpoint = (
            f'"repos/${{{self.repo_variable()}}}/private-vulnerability-reporting"'
        )
        api_call = RemoteVersionController.I.api_method_args(
            endpoint=endpoint,
            method="PUT",
        )
        return f"""{self.vulnerability_reporting_function()}() {{
  {api_call}
}}"""

    def vulnerability_reporting_function(self) -> str:
        """Return `"vulnerability_reporting"`, the function name."""
        return "vulnerability_reporting"
