#   -------------------------------------------------------------
#   Copyright (c) Hexafuchs. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
"""This defines types related to ids."""
from __future__ import annotations

from sys import version_info

if version_info[0] > 3 or version_info[1] >= 10:
    from typing import TypeAlias

__all__ = ["SharkeyId"]

if version_info[0] > 3 or version_info[1] >= 10:
    """The current representation of an ID in Sharkey."""
    SharkeyId: TypeAlias = str
else:
    SharkeyId = str
