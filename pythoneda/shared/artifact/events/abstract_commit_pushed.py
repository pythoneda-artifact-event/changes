# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/abstract_commit_pushed.py

This file declares the AbstractCommitPushed event.

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
from .change_event import ChangeEvent
from pythoneda.shared import primary_key_attribute
from typing import List


class AbstractCommitPushed(ChangeEvent):
    """
    Represents the moment a commit has been pushed.

    Class name: AbstractCommitPushed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        change: Change,
        commit: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new AbstractCommitPushed instance.
        :param change: The committed change.
        :type change: pythoneda.shared.artifact.events.Change
        :param commit: The commit.
        :type commit: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param previousEventId: The id of previous events, if any.
        :type previousEventId: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._commit = commit
        super().__init__(change, previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def commit(self) -> str:
        """
        Retrieves the commit.
        :return: Such value.
        :rtype: str
        """
        return self._commit


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
