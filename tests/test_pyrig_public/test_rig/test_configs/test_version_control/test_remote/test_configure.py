"""Test module."""

from pyrig.rig.configs.version_control.remote.configure import (
    ConfigureRepositoryConfigFile as BaseConfigureRepositoryConfigFile,
)

from pyrig_public.rig.configs.version_control.remote.configure import (
    ConfigureRepositoryConfigFile,
)
from pyrig_public.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class TestConfigureRepositoryConfigFile:
    """Test class."""

    def test_scripts(self) -> None:
        """Test method."""
        script = ConfigureRepositoryConfigFile.I
        assert script.scripts() == (
            *BaseConfigureRepositoryConfigFile().scripts(),
            script.fork_pr_contributor_approval_script(),
            script.vulnerability_reporting_script(),
        )

    def test_fork_pr_contributor_approval_script(self) -> None:
        """Test method."""
        script = ConfigureRepositoryConfigFile.I
        settings = RepositorySettingsConfigFile.I
        result = script.fork_pr_contributor_approval_script()
        assert result.startswith("fork_pr_contributor_approval() {")
        assert (
            f"jq '.{settings.fork_pr_contributor_approval_key()}' "
            f"{settings.path().as_posix()}"
        ) in result
        assert "actions/permissions/fork-pr-contributor-approval" in result
        assert "--method=PUT" in result
        assert "--input=-" in result

    def test_fork_pr_contributor_approval_function(self) -> None:
        """Test method."""
        assert (
            ConfigureRepositoryConfigFile.I.fork_pr_contributor_approval_function()
            == RepositorySettingsConfigFile.I.fork_pr_contributor_approval_key()
        )

    def test_vulnerability_reporting_script(self) -> None:
        """Test method."""
        script = ConfigureRepositoryConfigFile.I
        result = script.vulnerability_reporting_script()
        assert result.startswith("vulnerability_reporting() {")
        assert "private-vulnerability-reporting" in result
        assert "--method=PUT" in result

    def test_vulnerability_reporting_function(self) -> None:
        """Test method."""
        assert (
            ConfigureRepositoryConfigFile.I.vulnerability_reporting_function()
            == "vulnerability_reporting"
        )
