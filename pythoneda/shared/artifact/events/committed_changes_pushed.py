# vim: set fileencoding=utf-8
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
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new CommittedChangesPushed instance.
        :param change: The committed change.
        :type change: pythoneda.shared.artifact.events.Change
        :param commit: The commit.
        :type commit: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            change,
            commit,
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
