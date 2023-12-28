"""
pythoneda/shared/artifact/events/committed_changes_pushed.py

This file declares the CommittedChangesPushed event.

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
from .abstract_commit_pushed import AbstractCommitPushed
from .change import Change
from typing import List


class CommittedChangesPushed(AbstractCommitPushed):
    """
    Represents the moment committed changes have been pushed.

    Class name: CommittedChangesPushed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact.events.StagedChangesCommitted: The event this one is response to.
    """

    def __init__(
        self,
        change: Change,
        commit: str,
        stagedChangesCommittedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CommittedChangesPushed instance.
        :param change: The committed change.
        :type change: pythoneda.shared.artifact.events.Change
        :param commit: The commit.
        :type commit: str
        :param stagedChangesCommittedId: The id of the request event.
        :type stagedChangesCommittedId: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            change,
            commit,
            stagedChangesCommittedId,
            reconstructedId,
            reconstructedPreviousEventIds,
        )
