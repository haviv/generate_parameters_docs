**Field Name:** beginMoveBackStepLink

**Description:** The `beginMoveBackStepLink` field in Pathlock Cloud's email template system is used to generate a hyperlink within an email that allows users to move a step within a workflow process back to a previous step. This feature is a part of the workflow management system, enabling users to revisit earlier stages of an approval or a review process.

**Usage Context:** This field is typically used in email templates that are sent as part of various workflow processes. It is particularly applicable in scenarios where action needs to be taken on a step in the workflow, such as moving a step back to a prior stage, to facilitate revisions or re-evaluations in workflow processes.

**Example:** 

Move step back: $$beginMoveBackStepLink$$

After rendering:

Move step back:  
<a href="https://cloud.pathlock.com/stepMoveBack?id=45321&action=3">Move Back</a>