# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/docker_image_requested.py

This file declares the DockerImageRequested event.

Copyright (C) 2024-today rydnr's pythoneda-shared-artifact/events

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
from .abstract_docker_event import AbstractDockerEvent
from pythoneda.shared import primary_key_attribute
from typing import Dict, List


class DockerImageRequested(AbstractDockerEvent):
    """
    Represents the moment a Docker image is requested.

    Class name: DockerImageRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        imageName: str,
        imageVersion: str = "latest",
        metadata: Dict[str, str] = {},
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new DockerImageRequested instance.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The image version.
        :type imageVersion: str
        :param metadata: The image metadata.
        :type metadata: Dict[str, str]
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            imageName,
            imageVersion,
            metadata,
            previousEventIds,
            reconstructedId,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
