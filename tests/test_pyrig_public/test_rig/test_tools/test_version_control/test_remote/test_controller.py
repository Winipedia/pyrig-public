"""Test module."""

from pyrig_public.rig.tools.version_control.remote.controller import (
    RemoteVersionController,
)


class TestRemoteVersionController:
    """Test class."""

    def test_security_advisory_url(self) -> None:
        """Test method."""
        controller = RemoteVersionController.I
        assert controller.security_advisory_url() == (
            f"{controller.repo_url()}/security/advisories/new"
        )
