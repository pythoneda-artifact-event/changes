# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/change_staged.py

This file declares the ChangeStaged event.

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
from pythoneda.shared import Event, primary_key_attribute
from typing import List


class ChangeStaged(Event):
    """
    Represents the moment a new change has been staged.

    Class name: ChangeStaged

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        change: Change,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new ChangeStaged instance.
        :param change: The change information.
        :type change: pythoneda.shared.artifact.events.Change
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._change = change
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def change(self) -> Change:
        """
        Retrieves the change.
        :return: Such information.
        :rtype: pythoneda.shared.artifact.events.Change
        """
        return self._change


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
