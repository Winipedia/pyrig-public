"""Test module."""

from pyrig_public.rig.configs.community.security import SecurityConfigFile
from pyrig_public.rig.tools.version_control.remote.controller import (
    RemoteVersionController,
)


class TestSecurityConfigFile:
    """Test class."""

    def test_reporting_method(self) -> None:
        """Test method."""
        result = SecurityConfigFile.I.reporting_method()
        url = RemoteVersionController.I.security_advisory_url()
        assert result == f"[GitHub's private vulnerability reporting]({url})"
