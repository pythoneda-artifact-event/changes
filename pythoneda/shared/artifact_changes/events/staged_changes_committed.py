"""
pythoneda/shared/artifact_changes/events/staged_changes_committed.py

This file declares the StagedChangesCommitted event.

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
from pythoneda import Event, primary_key_attribute
from pythoneda.shared.artifact_changes import Change
from typing import List

class StagedChangesCommitted(Event):
    """
    Represents the moment staged changes have been committed.

    Class name: StagedChangesCommitted

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact_changes.events.ChangeStagingCodeDescribed: The event this one is response to.
    """

    def __init__(
        self,
        change: Change,
        commit: str,
        changeStagingCodeDescribedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new StagedChangesCommitted instance.
        :param change: The change information.
        :type change: pythoneda.shared.artifact_changes.Change
        :param commit: The hash of the commit.
        :type commit: str
        :param changeStagingCodeDescribedId: The id of the request event.
        :type changeStagingCodeDescribedId: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if changeStagingCodeDescribedId:
            previous_events = [changeStagingCodeDescribedId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._change = change
        self._commit = commit

    @property
    @primary_key_attribute
    def change(self) -> Change:
        """
        Retrieves the change.
        :return: Such information.
        :rtype: pythoneda.shared.artifact_changes.Change
        """
        return self._change

    @property
    @primary_key_attribute
    def commit(self) -> str:
        """
        Retrieves the commit.
        :return: Such information.
        :rtype: str
        """
        return self._commit
