"""
pythoneda/shared/artifact_commit/events/artifact_commit_tagged.py

This file declares the ArtifactCommitTagged event.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-commit/events

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
from .abstract_commit_tagged import AbstractCommitTagged
from typing import List


class ArtifactCommitTagged(AbstractCommitTagged):
    """
    Represents the moment a commit in the artifact repository of a domain has been tagged.

    Class name: ArtifactCommitTagged

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact_commit.events.ArtifactChangesCommitted: A previous event that wraps the commit.
    """

    def __init__(
        self,
        tag: str,
        commit: str,
        repositoryUrl: str,
        branch: str,
        repositoryFolder: str,
        artifactChangesCommittedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CommitTagged instance.
        :param tag: The tag.
        :type tag: str
        :param commit: The hash of the commit.
        :type commit: str
        :param repositoryUrl: The repository url.
        :type repositoryUrl: str
        :param repositoryFolder: The repository folder.
        :param branch: The branch.
        :type branch: str
        :type repositoryFolder: str
        :param artifactChangesCommittedId: The id of the previous event, if any.
        :type artifactChangesCommittedId: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            tag,
            commit,
            repositoryUrl,
            branch,
            repositoryFolder,
            artifactChangesCommittedId,
            reconstructedId,
            reconstructedPreviousEventIds)
