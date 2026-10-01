"""Repository-level settings and protection ruleset configuration for GitHub."""

from typing import Any

from pyrig.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as BaseRepositorySettingsConfigFile,
)


class RepositorySettingsConfigFile(BaseRepositorySettingsConfigFile):
    """Override repository settings for public GitHub repositories."""

    def _configs(self) -> dict[str, Any]:
        """Add public visibility and fork-PR approval to the base settings.

        Returns:
            The inherited settings with public visibility and approval
            required for external contributors' fork pull request workflows.
        """
        configs = super()._configs()
        configs[self.repository_key()]["visibility"] = self.visibility()
        configs[self.fork_pr_contributor_approval_key()] = {
            "approval_policy": self.fork_pr_contributor_approval_policy(),
        }
        return configs

    def fork_pr_contributor_approval_key(self) -> str:
        """Return `"fork_pr_contributor_approval"`.

        The top-level key for the fork pull request contributor approval
        policy, i.e. which external contributors must be approved by a
        maintainer before their fork PR's workflows run.
        """
        return "fork_pr_contributor_approval"

    def fork_pr_contributor_approval_policy(self) -> str:
        """Return the approval policy for fork pull request contributors."""
        return "all_external_contributors"

    def visibility(self) -> str:
        """Return the visibility value applied to the repository.

        Returns:
            `public`, the visibility required by this public-repository plugin.
        """
        return "public"
