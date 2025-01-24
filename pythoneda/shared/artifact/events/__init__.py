# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/__init__.py

This file ensures pythoneda.shared.artifact.events is a namespace.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/events

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import sys

from .change import Change
from .change_event import ChangeEvent
from .abstract_changes_committed import AbstractChangesCommitted
from .abstract_commit_pushed import AbstractCommitPushed
from .abstract_commit_tagged import AbstractCommitTagged
from .abstract_docker_event import AbstractDockerEvent
from .abstract_tag_pushed import AbstractTagPushed
from .change_staged import ChangeStaged
from .change_staging_from_folder_requested import ChangeStagingFromFolderRequested
from .committed_changes_pushed import CommittedChangesPushed
from .committed_changes_tagged import CommittedChangesTagged
from .docker_image_available import DockerImageAvailable
from .docker_image_failed import DockerImageFailed
from .docker_image_requested import DockerImageRequested
from .docker_image_push_failed import DockerImagePushFailed
from .docker_image_push_requested import DockerImagePushRequested
from .docker_image_pushed import DockerImagePushed
from .staged_changes_committed import StagedChangesCommitted
from .tag_pushed import TagPushed

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
