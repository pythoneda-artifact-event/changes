"""
pythoneda/shared/artifact_changes/events/staged_changes_commit_code_requested.py

This file declares the StagedChangesCommitCodeRequested event.

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

class StagedChangesCommitCodeRequested(Event):
    """
    Represents the moment code to commit staged changes is requested.

    Class name: StagedChangesCommitCodeRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        repositoryUrl: str,
        branch: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new StagedChangesCommitCodeRequested instance.
        :param repositoryUrl: The repository url.
        :type repositoryUrl: str
        :param branch: The branch.
        :type branch: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            previousEventIds, reconstructedId, reconstructedPreviousEventIds
        )
        self._repository_url = repositoryUrl
        self._branch = branch

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository.
        :return: Such information.
        :rtype: str
        """
        return self._repository_url

    @property
    @primary_key_attribute
    def branch(self) -> str:
        """
        Retrieves the branch.
        :return: Such information.
        :rtype: str
        """
        return self._branch
