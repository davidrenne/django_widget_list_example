![alt text](web/app/images/velocity.png "Velocity")

## Github to Redmine Custom Integrations ##

### Updates ###

* 10/15/2018: Previously when you update a ticket the `#tbd` `#working` `#resolved` did not assign to you.

### Purpose ###

The primary objective of these integration hooks are to sync github commits to existing tickets to show transparency of affected files and history of changes before/after testing is completed.  Additionally it is to allow a developer to not have to be logged into redmine "filing paper work" and filling out fields we already know about (such as current version and where new features and tickets go).

An examples could be, that TSE asks us to fix something and we get it done right away.  You would simply put #velocitybug in your commit message and type #resolved which will assign it to Nathan and reference your commit in the ticket for him to verify and test.

### Source Code Locations ###

[Push Hooks inside Studio
](https://github.com/atlonaeng/studio/blob/master/gitWebHooks/hooks.go#L146)

[Go Core server mount
](https://github.com/DanielRenne/GoCore/blob/master/core/app/app.go#L231-L268)

### Webconfig To Setup ###

There are 4 main JSON configs in gocore to set it up locally to make changes.

```
   "application":{
      "mountGitWebHooks": true,
      "gitWebHookPath": "/webhooks",
      "gitWebHookSecretKey": "922797c796c415c69a1bf1e7667f535b37c9f36e",
      "gitWebHookServerPort": "12345",
```

By default if you setup a new githook, you must set the payload type as json pointing to your IP address and port to recieve.

I like setting this up locally so that when people push new commits, my computer just talks to me so I am aware of what is changing without looking online at github.

There should only be one IP address which has a gateway which has a dontTouch file.  This dontTouch file is the way in which a gateway's webConfig is not overwritten each firmware update and this is the gateway which will be inserting and updating redmine tickets for you.

```
				if extensions.DoesFileExist(goPath + "/src/github.com/atlonaeng/studio/webConfig.dontTouch") {

```

### Development Team Standards and How To Use ###

#### Overview example ####


From now on, all commits are being tracked into a Redmine ticket regardless of what you commit against.  We all need to follow this procedure as best as possible.  If you push a commit without a new ticket being created or referencing an old one, it will be dumped as a comment into the current catch all tickets:

* [Velocity Catch All
](http://qa.atlona.com/issues/6869)

* [AMS Catch All
](http://qa.atlona.com/issues/6870)

If you are working on a known ticket you must commit a message like the following example I am working on ticket 6872.  I would commit like this if I am done with the ticket.

```
6872: This should resolve all issues now #resolved
```

[Here is an example of what it would look like when you push an existing ticket which is resolved.
](http://qa.atlona.com/issues/6872#note-3)

An example commit which would update the catch all would be any sentence which doesnt contain the "New Ticket Hashtags" or referencing an old ticket via `INT:` in the begining of your commit message.

#### A note about closed tickets which you push new code against ####

If a ticket is closed and you push new code, currently the system will re-open it with a message that it was automatically reopened and it will assign to Harsha or Nathan automatically because you pushed code against something that is done already and it might need more testing after the fact

#### Caveats about the catch all tickets ####

Currently Reza and Kat's commits which are untracked will ALWAYS go into the AMS buckets.  It is hard coded on line 

```
   if !shouldInsertNew && (info.Pusher.Name == "frezadev" || info.Pusher.Name == "katsacca") {
```

If either Kathryn or Reza are mostly working back on velocity, they can remove themselves to fall into the below elseif 

```
					} else if !shouldInsertNew {
						// Velocity
						hasUpdate = true
						issueToUpdate = CURRENT_VELOCITY_CATCH_ALL_TICKET
					}
```

#### Creating new bugs and features for AMS and Velocity (#hashtag keywords) ####

##### Global hashtags #####

On new tickets using `#velocityfeature` `#velocitybug` `#amsbug` `#amsfeature`.  By default these are set in a new status and assigned to yourself.  But you can use the below to do nice things like resolving them right away or put into the TBD buckets.

* `#resolved` will resolve a new ticket immediately on creation or resolve an old one.  Any resolved updates on new or existing tickets should automatically assign to Nathan for Velocity and Harsha for AMS.
* `#tbd` by default all tickets are created in the current master sprint (so 1.5.0 is current master in velocity right now).  But if you say `#tbd`, it will create the ticket into the rainy day buckets
* `#working` you are not done yet, it will assign as 10% done and say it's "In Progress" on Redmine and keep assigned to you.

##### Syntax for updating tickets #####

* You must start all tickets with `INT:`, where int is the ticket number and you must have a colon and then a message.  You may use any global hashtags above, but do not intermix "New Ticket Hashtags" when you reference a bug because it will probably update and insert a new one (i've never tested it like that)

##### AMS (New Ticket Hashtags) #####

* `#amsbug` or `#ab` Insert a new ams bug
* `#amsfeature` or `#af` Insert a new ams feature into the latest build

##### Velocity (New Ticket Hashtags) #####

* `#velocitybug` or `#vb` Insert a new velocity bug
* `#velocityfeature ` or `#vf` Insert a new velocity feature into the latest build

### Maintenance of Current Versions and procedures ###

There is now a process where, when a release goes out (like 1.5.0 now) and master is now going to become 1.6.0.  A developer must manually create a ticket for an AMS bucket and a Velocity catch all bucket for commits which are not tagged to a ticket.

Examples are like these:

* [Velocity Catch All
](http://qa.atlona.com/issues/6869)

* [AMS Catch All
](http://qa.atlona.com/issues/6870)

Once you create this new ticket, you must reference them in the code and push a build to the final service server who is processing the hooks.

Update

```
	CURRENT_VELOCITY_CATCH_ALL_TICKET = ???YOURNEWTICKET??
	CURRENT_AMS_CATCH_ALL_TICKET = ???YOURNEWTICKET??
```

When you shift to the next iteration, someone on the team must also update the firmware version in the code.  You can just view source in a ticket to get the ID's for the next firmware.

```
	CURRENT_VELOCITY_REDMINE_VERSION  = 184  // 1.5 release
	CURRENT_AMS_REDMINE_VERSION       = 275  // 2.0.15 release
```
