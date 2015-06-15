# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import ASCIILine
from gs.auth.token import AuthToken


class ILeaveGroup(Interface):
    'Leave a group'
    userId = ASCIILine(
        title='User ID',
        description='The identifier of the person who is leaving the group',
        required=True)

    groupId = ASCIILine(
        title='Group ID',
        description='The identifier of the group that the user is leaving',
        required=True)

    token = AuthToken(
        title='Token',
        description='The authentication token',
        required=True)
