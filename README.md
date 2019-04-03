## Soft deletion demo app

A small, toy Django app to illustrate some of the issues with using `SoftDeletableModel`.

The tests demonstrate exactly the same code running against "normal" models and soft-deletable models.

To run the tests:

```bash
pip install -r requirements.txt  # recommend using a virtualenv or Pipenv
./manage.py test -v2
```

Output:

```
...
test_counts (groups.tests.NormalTestCase) ... ok
test_deleted_musician (groups.tests.NormalTestCase) ... ok
test_counts (groups.tests.SoftDeletableTestCase) ... FAIL
test_deleted_musician (groups.tests.SoftDeletableTestCase) ... FAIL

======================================================================
FAIL: test_counts (groups.tests.SoftDeletableTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mozz/Documents/Source/personal/soft_deletion/groups/tests.py", line 29, in test_counts
    self.assertEqual(3, the_beatles.num_members)
AssertionError: 3 != 4

======================================================================
FAIL: test_deleted_musician (groups.tests.SoftDeletableTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mozz/Documents/Source/personal/soft_deletion/groups/tests.py", line 18, in test_deleted_musician
    self.assertEqual(3, self.beatles.members.count())
AssertionError: 3 != 4

----------------------------------------------------------------------
Ran 4 tests in 0.046s

FAILED (failures=2)
...
```