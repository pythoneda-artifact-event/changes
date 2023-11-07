"""
pythoneda/shared/artifact/events/abstract_tag_pushed.py

This file declares the AbstractTagPushed class.

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
from pythoneda import attribute, Event, primary_key_attribute
from typing import List


class AbstractTagPushed(Event):
    """
    Base class for XTagPushed events.

    Class name: AbstractTagPushed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        tag: str,
        commit: str,
        repositoryUrl: str,
        branch: str,
        repositoryFolder: str,
        committedChangesTaggedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new AbstractTagPushed instance.
        :param tag: The tag.
        :type tag: str
        :param commit: The hash of the commit.
        :type commit: str
        :param repositoryUrl: The repository url.
        :type repositoryUrl: str
        :param branch: The branch.
        :type branch: str
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param committedChangesTaggedId: The id of the previous event, if any.
        :type committedChangesTaggedId: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if committedChangesTaggedId:
            previous_events = [committedChangesTaggedId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._tag = tag
        self._commit = commit
        self._repository_url = repositoryUrl
        self._branch = branch
        self._repository_folder = repositoryFolder

    @property
    @primary_key_attribute
    def tag(self) -> str:
        """
        Retrieves the tag.
        :return: Such information.
        :rtype: str
        """
        return self._tag

    @property
    @primary_key_attribute
    def commit(self) -> str:
        """
        Retrieves the commit.
        :return: Such information.
        :rtype: str
        """
        return self._commit

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the repository url.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url

    @property
    @attribute
    def branch(self) -> str:
        """
        Retrieves the branch.
        :return: Such information.
        :rtype: str
        """
        return self._branch

    @property
    @primary_key_attribute
    def repository_folder(self) -> str:
        """
        Retrieves the repository folder.
        :return: Such folder.
        :rtype: str
        """
        return self._repository_folder
