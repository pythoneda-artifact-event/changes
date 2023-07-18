"""
pythonedaartifactchangesevents/change_staging_requested.py

This file declares the ChangeStagingRequested event.

Copyright (C) 2023-today rydnr's pythoneda-artifact-changes/events

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
from pythoneda.event import Event
from pythoneda.value_object import primary_key_attribute
from pythonedaartifactchangesshared.change import Change
from typing import List

class ChangeStagingRequested(Event):
    """
    Represents the moment a new change is requested to be staged.

    Class name: ChangeStagingRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self, change:Change, previousEventIds:List[str]=None, reconstructedId:str=None, reconstructedPreviousEventIds:List[str]=None):
        """
        Creates a new ChangeStagingRequested instance.
        :param change: The change information.
        :type change: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(previousEventIds, reconstructedId, reconstructedPreviousEventIds)
        self._change = change

    @property
    @primary_key_attribute
    def change(self) -> Change:
        """
        Retrieves the change.
        :return: Such information.
        :rtype: pythonedaartifactsharedchanges.change.Change
        """
        return self._change
