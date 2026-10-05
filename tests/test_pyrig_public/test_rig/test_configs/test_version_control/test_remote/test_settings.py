"""Test module."""

from pyrig_public.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class TestRepositorySettingsConfigFile:
    """Test class."""

    def test_settings(self) -> None:
        """Test method."""
        settings = RepositorySettingsConfigFile.I
        configs = settings.settings()
        key = settings.fork_pr_contributor_approval_key()
        repository_key = settings.repository_key()
        assert configs[repository_key]["visibility"] == settings.visibility()
        assert configs[key] == {
            "approval_policy": settings.fork_pr_contributor_approval_policy(),
        }

    def test_fork_pr_contributor_approval_key(self) -> None:
        """Test method."""
        assert (
            RepositorySettingsConfigFile.I.fork_pr_contributor_approval_key()
            == "fork_pr_contributor_approval"
        )

    def test_fork_pr_contributor_approval_policy(self) -> None:
        """Test method."""
        assert (
            RepositorySettingsConfigFile.I.fork_pr_contributor_approval_policy()
            == "all_external_contributors"
        )

    def test_visibility(self) -> None:
        """Test method."""
        assert RepositorySettingsConfigFile.I.visibility() == "public"
