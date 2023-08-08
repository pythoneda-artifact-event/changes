"""
pythoneda/shared/artifact_changes/events/__init__.py

This file ensures pythoneda.shared.artifact_changes.events is a namespace.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .staged_changes_committed import StagedChangesCommitted
from .change_staged import ChangeStaged
from .change_staging_code_described import ChangeStagingCodeDescribed
from .change_staging_code_requested import ChangeStagingCodeRequested
from .change_staging_from_folder_requested import ChangeStagingFromFolderRequested
from .staged_changes_commit_code_requested import StagedChangesCommitCodeRequested
