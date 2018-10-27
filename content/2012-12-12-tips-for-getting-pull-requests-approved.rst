Tips for getting pull requests approved
#######################################
:date: 2012-12-12 12:50
:author: Russell Ballestrini
:tags: Code, Greatest Hits, Opinion
:slug: tips-for-getting-pull-requests-approved
:status: published

.. contents::


Pull rejection sucks!
================================================


You have just coded, implemented, and submitted a pull request. A short
while later the request is declined by an upstream maintainer and you
feel crushed. We have all been there. Today I'm going to show you a
better way. This article will teach you how to create pull requests that
get approved.

Start small
================================================

You need to earn trust with the maintainers. Your first commit should be
a small change which they *cannot* reject. Try to write a missing test
or re-factor duplicate code. Correct a comment's accuracy or rename a
variable to better reflect its purpose. Your first pull request should
not alter how the program works.

|start-small.xcf|

Don't add leading or trailing white space
================================================

Additional whitespace will alter the diff output. This causes version
control systems to flag lines as changed which is irritating and
sometimes misleading.

|spot-the-diff.xcf|

Less is more
================================================

Minimize the number of changes to accomplish your goal. People are busy
and at times lazy. Reduce the work the maintainers must do to perform a
merge. Lowering the amount of lines to review should increase the chance
of approval.

|less-is-more.xcf|

Only commit working code
================================================

Do not break the program, only commit working code. If the project has
tests make sure they work before you commit.

|commit-working-code.xcf|

Follow the leader
================================================

Try to mimic the maintainers. Follow the coding style and project layout
even if it seems wrong. This is not your playground... yet. Before you
commit, review the VCS logs to learn how verbose or terse your commit
messages should be. When in Rome do as the romans do. This silly game of
follow the leader reduces friction of an outsider committing to the
project.

|follow-the-leader.xcf|

Comments, docs, and tests oh my!
================================================

Your first pull request should clarify or add to the existing
documentation. Fix the README, adjust a comment, or write a test. These
tasks might appear small but they serve to prove that you possess
comprehension of the source code. They also do not alter the program's
functionality.

Having a few of these pull requests under-your-belt will
earn you trust which will eventuality translate to more responsibility in
the future. You will also differentiate yourself from the rest because
most people do not enjoy working on documentation.

|comments-docs-tests-oh-my.xcf|

Blog about the change
================================================

Write about the change, give reasons and examples. Include a link to
your blog post in the pull request.

|ideas-blog-get-heard.xcf|

Pull requests are like paragraphs
================================================

If you were writing an essay, you would split up your ideas into
separate paragraphs. A pull request has many qualities similar to a
paragraph. Each commit should be related to the pull request's main
objective. Commits of a pull request should stay focused and on topic.

    | A pull request is to a program as a paragraph is to an essay.
    |  A commit is to a pull request as a sentence is to a paragraph.

In an essay, if you have more then one topic you should have more then
one paragraph. Likewise when coding, only one idea or change per pull
request.

Separating your ideas into different pull requests will grant the
maintainers greater flexibility when they begin to integrate. They will
have the ability to pick-and-choose which requests to merge and
everybody wins!

|pull-request-stay-focused.xcf|



.. |start-small.xcf| image:: /uploads/2012/12/start-small.xcf_.png
   :target: /uploads/2012/12/start-small.xcf_.png
.. |spot-the-diff.xcf| image:: /uploads/2012/12/spot-the-diff.xcf_.png
   :target: /uploads/2012/12/spot-the-diff.xcf_.png
.. |less-is-more.xcf| image:: /uploads/2012/12/less-is-more.xcf_.png
   :target: /uploads/2012/12/less-is-more.xcf_.png
.. |commit-working-code.xcf| image:: /uploads/2012/12/commit-working-code.xcf_.png
   :target: /uploads/2012/12/commit-working-code.xcf_.png
.. |follow-the-leader.xcf| image:: /uploads/2012/12/follow-the-leader.xcf_.png
   :target: /uploads/2012/12/follow-the-leader.xcf_.png
.. |comments-docs-tests-oh-my.xcf| image:: /uploads/2012/12/comments-docs-tests-oh-my.xcf_.png
   :target: /uploads/2012/12/comments-docs-tests-oh-my.xcf_.png
.. |ideas-blog-get-heard.xcf| image:: /uploads/2012/12/ideas-blog-get-heard.xcf_.png
   :target: /uploads/2012/12/ideas-blog-get-heard.xcf_.png
.. |pull-request-stay-focused.xcf| image:: /uploads/2012/12/pull-request-stay-focused.xcf_.png
   :target: /uploads/2012/12/pull-request-stay-focused.xcf_.png
