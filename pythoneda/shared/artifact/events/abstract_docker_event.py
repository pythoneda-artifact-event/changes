# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/abstract_docker_event.py

This file declares the AbstractDockerEvent event.

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
import abc
from pythoneda.shared import attribute, Event, primary_key_attribute
from typing import Dict, List


class AbstractDockerEvent(Event, abc.ABC):
    """
    Base class for Docker-related events.

    Class name: AbstractDockerEvent

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        imageName: str,
        imageVersion: str,
        metadata: Dict[str, str] = None,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new AbstractDockerEvent instance.
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
        self._image_name = imageName
        self._image_version = imageVersion
        self._metadata = metadata
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def image_name(self) -> str:
        """
        The image name.
        :return: Such name.
        :rtype: str
        """
        return self._image_name

    @property
    @primary_key_attribute
    def image_version(self) -> str:
        """
        The image version.
        :return: Such version.
        :rtype: str
        """
        return self._image_version

    @property
    @attribute
    def metadata(self) -> Dict[str, str]:
        """
        The image metadata.
        :return: Such metadata.
        :rtype: Dict[str, str]
        """
        return self._metadata


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
