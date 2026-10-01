"""Configuration management for SECURITY.md files.

Manages SECURITY.md, the project's vulnerability-reporting policy.
"""

from pyrig.rig.configs.community.security import (
    SecurityConfigFile as BaseSecurityConfigFile,
)

from pyrig_public.rig.tools.version_control.remote.controller import (
    RemoteVersionController,
)


class SecurityConfigFile(BaseSecurityConfigFile):
    """Override the default security policy for public repositories."""

    def reporting_method(self) -> str:
        """Return a Markdown link to the repository's private reporting form.

        Returns:
            Link to GitHub's private vulnerability reporting form.
        """
        url = RemoteVersionController().security_advisory_url()
        return f"[GitHub's private vulnerability reporting]({url})"
