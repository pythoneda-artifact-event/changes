# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/committed_changes_tagged.py

This file declares the CommittedChangesTagged event.

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
from .abstract_commit_tagged import AbstractCommitTagged
from typing import List


class CommittedChangesTagged(AbstractCommitTagged):
    """
    Represents the moment a commit has been tagged.

    Class name: CommittedChangesTagged

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact.events.StagedChangesCommitted: A previous event that wraps the commit.
    """

    def __init__(
        self,
        tag: str,
        commit: str,
        repositoryUrl: str,
        branch: str,
        repositoryFolder: str,
        stagedChangesCommittedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CommittedChangesTagged instance.
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
        :param stagedChangesCommittedId: The id of the previous event, if any.
        :type stagedChangesCommittedId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            tag,
            commit,
            repositoryUrl,
            branch,
            repositoryFolder,
            stagedChangesCommittedId,
            reconstructedId,
            reconstructedPreviousEventIds,
        )
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
