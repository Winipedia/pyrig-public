"""Identity, URL, and environment metadata for a repository's remote hosting service."""

from pyrig.rig.tools.version_control.remote.controller import (
    RemoteVersionController as BaseRemoteVersionController,
)


class RemoteVersionController(BaseRemoteVersionController):
    """Override the base remote version controller for public repositories."""

    def security_advisory_url(self) -> str:
        """Construct the URL for filing a new private security advisory.

        Returns:
            URL in the format
            `https://github.com/{owner}/{repo}/security/advisories/new`.
        """
        return f"{self.repo_url()}/security/advisories/new"
