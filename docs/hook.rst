========
Web hook
========

Synopsis
========

``/gs-group-member-leave.json``? :option:`token` =<t> & :option:`groupId` = <g> & :option:`userId` =<u> & :option:`leave`

Description
===========

The ``gs-group-member-leave.json`` page in the **site** context
removes a person from the group.

Required arguments
==================

.. option:: token

  The authentication token [#token]_.

.. option:: groupId=<groupId>

  The identifier for the group.

.. option:: userId=<userId>

  The identifier for the user.

.. option:: leave

   The "form" action. (No value needs to be set, but the argument
   must be present)

Returns
=======

In response a JSON_ object will be returned with the following
values:

.. js:class:: LeaveResponse()

   .. js:attribute:: status

      The exist status:

      * ``0``: Success, the person has been removed from the
        group.
      * ``1``: No such group.
      * ``2``: No such user.
      * ``4``: The user and group exist, but the user is not a
        member of the group.

   .. js:attribute:: message

      The plain-text version of the :js:attr:`status`.

   .. js:attribute:: groupId

      The identifier for the group that the person was removed from.

   .. js:attribute:: userId:

      The identifier of user-profile of the person that was
      removed from the group.

Example
=======

Using :program:`wget` to remove the person with the
user-identifier ``qK7SgjsTHcLNrJ2ClevcJ0`` from the group
``test``.

.. code-block:: console

   $ wget --post-data='token=Fake&groupId=test&userId=qK7SgjsTHcLNrJ2ClevcJ0&leave' \
     http://groups.example.com/gs-group-member-leave.json

The response will look similar to the following:

.. code-block:: json

   {
     "status": 0,
     "message": "A Person has left Test",
     "groupId": "test",
     "userId": "qK7SgjsTHcLNrJ2ClevcJ0"
   }

.. [#token] See ``gs.auth.token``
             <https://github.com/groupserver/gs.auth.token/>

.. _JSON: http://json.org/
