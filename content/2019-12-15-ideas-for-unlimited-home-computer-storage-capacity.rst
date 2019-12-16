Dreaming of unlimited home computer storage capacity
#####################################################

:author: Russell Ballestrini
:slug: dreaming-of-unlimited-home-computer-storage-capacity
:date: 2019-12-15 09:52
:tags: Idea
:status: published

Unlimited computer storage capacity is a common science fiction trope and fun thought experiment.

What would be possible if we could potentially store near infinite data at your house in a normal sized desktop computer?

Even better using today's tech, what ideas could we dream up?

This post will explore ideas as we surf the bleeding edge of home computing.

Idea 1
==========

Live stream everything in your life in HD and store it locally at your house as a hyper real augment reality. A person could store and recall any event that he or she has witnessed using a headcam with wifi syncing capabilities.

    One of the many new features within the iPhone 6s is the ability for the 12MP camera on the back to record 4K video. It’s a big selling point for Apple, but what about storage space?

    According to a video published by MKBHD, just how much a one-minute long video shot in 4K will take up in your iPhone 6s’ storage has been discovered. According to the screenshot captured by Ryan Jones (@rjones) of the hands-on video, a one-minute video captured at 720p HD at 30fps will take up 60MB of space on the iPhone 6s. At 1080p HD and 30fps, it’s 130MB of space. A 1080p HD video at 60fps will take up 200MB of space. And, finally, the 4K video at 30fps will take up 375MB of space.

    reference: http://www.iphonehacks.com/2015/09/iphone-6s-4k-video-space.html

If we were streaming at 4k for 24 hours, it would be::

 >>> 60 * 24 * 375
 540000 

540,000MB or 540GB or .54TB per day of streaming everything.

A years worth of 4k streaming from some guys headcam would consume::

 >>> 365.25 * .54
 197.235

or 197TB worth of capacity. 

With today's technology and hardware available as home computing, including NAS systems, streaming 4k of a persons headcam would be possible... but not really practical without advancements in hard drive density.

A 6TB drive is $100, and by my math, we would need 34 drives (not really even counting for redundancy)::

 >>> 197.235 / 6
 32.8725

So the cost of a years worth a capacity would be::

 (197.235 / 6) * 100
 3287.25

or $3,287 for 34 x 6TB drives.

It would fit in an oversized NAS, just barely... in another section I'll figure out what hard drive density is needed to make 4k video at 30fps more practical.

Ok so, 4k streaming is currently not practical, so how about 1080p HD at 30fps? Could we do that with today's home tech?

One minute of 1080p HD at 30fps is 130MB of space.

If we were streaming at 1080p at 30fps for 24 hours, it would be::

 >>> 60 * 24 * 130
 187200 

187,200MB or 187GB or .187TB per day.

A years worth of non-stop 1080P streaming at 30fps off some guys headcam would consume::

 >>> 365.25 * .184
 67.235

Or about 68TB per year (rounded up).

Like before a 6TB drive is $100, and by my math, we would need 12 drives (not really even counting for redundancy)::

 >>> 67.206 / 6
 11.201 

so the cost of a years worth a capacity would be::

 >>> 12 * 100
 1200

or $1,200 for 12 x 6TB drives.

12 drives should easily fit in a mid-range home NAS. That said, a mid-range home NAS holding 12 drives is a clunky machine for most home owners.

It might be possible, but likely not practical without a support plan, in home repairs, and on-going maintenance.

It would likely require having a home NAS specialist in every region to offer up white gloved support for anyone who would be willing to pay for it.

How could we make this even easier with today's tech?

We could lower the quality even more...

Streaming 720P at 30fps you would need 36T per year or about 6 x 6TB drives for about $600 plus a NAS.

So at this time, if seems practical and economical to stream 720P at 30fps every minute of the year.

What would we need to build to make all this data useful?

Well we would need a way to index all this footage, and likely edit out useless footage.

We would need at least two headcams with wifi sync, so that we could have one charging while we use the other.

We would need software to sync the footage to the NAS, like ``syncthing``.

Besides that, all we need is some software to host the videos, edit, and index them to be searchable.




