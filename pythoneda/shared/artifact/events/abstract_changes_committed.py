"""
pythoneda/shared/artifact/events/abstract_changes_committed.py

This file declares the AbstractChangesCommitted class.

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
from pythoneda import attribute, primary_key_attribute
from typing import List


class AbstractChangesCommitted(ChangeEvent):
    """
    Base class for XChangesCommitted events.

    Class name: AbstractChangesCommitted

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        message: str,
        change: Change,
        commit: str,
        changeStagingCodeDescribedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new AbstractChangesCommitted instance.
        :param message: The message.
        :type message: str
        :param change: The change information.
        :type change: pythoneda.shared.artifact.events.Change
        :param commit: The hash of the commit.
        :type commit: str
        :param changeStagingCodeDescribedId: The id of the request event.
        :type changeStagingCodeDescribedId: str
        :param changeStagingCodeDescribedId: The id of previous event, if any.
        :type changeStagingCodeDescribedId: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            change,
            changeStagingCodeDescribedId,
            reconstructedId,
            reconstructedPreviousEventIds,
        )
        self._message = message
        self._commit = commit

    @property
    @attribute
    def message(self) -> str:
        """
        Retrieves the commit message.
        :return: Such message.
        :rtype: str
        """
        return self._message

    @property
    @primary_key_attribute
    def commit(self) -> str:
        """
        Retrieves the commit.
        :return: Such information.
        :rtype: str
        """
        return self._commit
