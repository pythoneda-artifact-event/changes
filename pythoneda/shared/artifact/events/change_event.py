"""
pythoneda/shared/artifact/events/change_event.py

This file declares the ChangeEvent class.

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
from .change import Change
from pythoneda import attribute, Event, primary_key_attribute
from pythoneda.shared.nix_flake import NixFlakeInput
from typing import List


class ChangeEvent(Event):
    """
    Events wrapping a Change.

    Class name: ChangeEvent

    Responsibilities:
        - Wraps all contextual information of the change.

    Collaborators:
        - None
    """

    def __init__(
        self,
        change: Change,
        previousEventId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ChangeEvent instance.
        :param change: The change information.
        :type change: pythoneda.shared.artifact.events.Change
        :param previousEventId: The id of the request event.
        :type previousEventId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if previousEventId:
            previous_events = [previousEventId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._change = change

    @property
    @primary_key_attribute
    def change(self) -> Change:
        """
        Retrieves the change.
        :return: Such information.
        :rtype: pythoneda.shared.artifact.events.Change
        """
        return self._change

    def matches_repository_folder(self, folder: str) -> bool:
        """
        Checks if this event is referring to given repository folder.
        :param folder: The folder to check.
        :type folder: str
        :return: True if the change is related to the repository folder; False otherwise.
        :rtype: bool
        """
        return self.change.repository_folder == folder

    def matches_input(self, target: NixFlakeInput) -> bool:
        """
        Checks if this event refers to given input.
        :param target: The input.
        :type target: pythoneda.shared.nix_flake.NixFlakeInput
        :return: True if the change is related to given input; False otherwise.
        :rtype: bool
        """
        return self.change.repository_url == target.url
