"""
pythonedaartifacteventchanges/staging_requested.py

This file declares the StagingRequested event.

Copyright (C) 2023-today rydnr's pythoneda-artifact-event/changes

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
from pythonedaactifactsharedchanges.change import Change
from typing import List

class StagingRequested(Event):
    """
    Represents the moment a new change is requested to be staged.

    Class name: StagingRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self, change:Change, previousEventId:str=None, id:str=None, previousEventIds:List[str]=None):
        """
        Creates a new StagingRequested instance.
        :param change: The change information.
        :type change: str
        :param previousEventId: The id of the previous event, if any.
        :type previousEventId: str
        :param id: The id of the event, if it's generated externally.
        :type id: str
        :param previousEventIds: The id of the previous events, if an external event is being recostructed.
        :type previousEventIds: List[str]
        """
        super().__init__(previousEventId, id, previousEventIds)
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
