# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/change_staging_from_folder_requested.py

This file declares the ChangeStagingFromFolderRequested event.

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
from pythoneda.shared import Event, primary_key_attribute
from typing import List


class ChangeStagingFromFolderRequested(Event):
    """
    Represents the moment changes from a folder are requested to be staged.

    Class name: ChangeStagingFromFolderRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        repositoryFolder: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ChangeStagingFromFolderRequested instance.
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            previousEventIds, reconstructedId, reconstructedPreviousEventIds
        )
        self._repository_folder = repositoryFolder

    @property
    @primary_key_attribute
    def repository_folder(self) -> str:
        """
        Retrieves the repository folder.
        :return: Such information.
        :rtype: str
        """
        return self._repository_folder
