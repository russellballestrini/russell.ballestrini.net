The Three Deployment Management Strategies
##########################################
:date: 2014-02-03 15:06
:author: Russell Ballestrini
:tags: DevOps, Opinion
:slug: the-three-deployment-management-strategies
:status: published

There are three deployment management strategies that could be used to
maintain a system. Each has pros and cons which I outline in this
document.

**run once**
    A proceedure that is run once and only once to setup a system's
    configuration values and settings. A semaphore or flag generally
    blocks repeated executions to prevent an undesirable outcome.

    Development Difficulty: LOW - binary state aware (has run/has not
    run)

**run always**
    A proceedure that is safe to run multiple times but uses a brute
    force method to setup a system's configuration and settings. It will
    self-heal at the expense of clobbering existing state.

    Development Difficulty: MEDIUM - not state aware - attention must be
    spent to allow multiple executions

**run as needed**
    A proceedure that is safe to run multiple times and checks a
    system's configuration and settings before it sets a system's
    configuration or settings. "checks before it steps". It will
    self-heal only the values it needs to.

    Development Difficulty: HIGH - state aware - must know how to both
    get and set values and make desicions based on what it finds.
