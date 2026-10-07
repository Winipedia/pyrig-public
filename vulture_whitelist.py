"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.string_ import StringConfigFile
from pyrig.rig.configs.community.security import (
    SecurityConfigFile as BaseSecurityConfigFile,
)

from pyrig_public.rig.configs.community.security import SecurityConfigFile
from pyrig_public.rig.configs.docs.api import APIDocsConfigFile

_CONFIG_FILE_OVERRIDES = (
    BaseSecurityConfigFile.reporting_method,
    ConfigFile.parent_path,
    ConfigFile.stem,
    StringConfigFile.content,
)
_CONFIG_FILES = (
    APIDocsConfigFile,
    SecurityConfigFile,
)
