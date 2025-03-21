# Comment For Parallel Step Returned Back

**Technical Name:** CommentForParallelStepReturnedBack

**Category:** Workflow

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter is used within the Pathlock Cloud GRC platform's workflow management system. It specifically applies to scenarios involving parallel steps in workflow instances. When a step is returned or requires revision, this parameter potentially allows for recording or tracking comments or notes associated with that action.

**Business Impact:**

Enabling comments for parallel steps that are returned for review or correction can enhance communication within the team, increase transparency, and improve the auditability of processes. It ensures that any issues or rationale for returning a step are clearly documented, facilitating a smoother resolution and progression of the workflow.

**Technical Impact when configured:**

When this parameter is enabled and configured, it allows users or automated processes to add comments to a step in a workflow that is sent back, especially in parallel processing scenarios. This can help in tracking the progress and reasons for any delays or revisions needed, thereby streamlining the process flow.

**Example Scenario:**

In a scenario where multiple departments are working on a shared project with parallel workflows, a step requiring approval from all departments may be returned by one department for correction. Using this parameter to annotate the reason for the return can guide the initiating team on the required corrections, thereby reducing the time to approval.

**Related Settings:** Not Applicable

**Best Practices:** 

- **Configure when:** You have workflows that involve parallel steps and require clear documentation and communication of any issues or feedback.
  
- **Avoid when:** The workflow is straightforward or does not involve parallel processing steps, to prevent unnecessary complexity or confusion.