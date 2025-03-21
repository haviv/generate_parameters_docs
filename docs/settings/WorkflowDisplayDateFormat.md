# Workflow Display Date Format

**Technical Name:** WorkflowDisplayDateFormat

**Category:** Configuration

**Default Value:** dd/MM/yyyy

**Impact Level:** Medium

**Description:**

The Workflow Display Date Format parameter controls the format in which dates are displayed within workflow-related communications and interfaces. It ensures that date information is consistently presented according to the regional or organizational preferences in the Pathlock Cloud GRC platform.

**Business Impact:**

Using a consistent date format across the platform improves clarity and prevents misunderstandings related to date-based information in workflows. It is especially significant in global, multi-regional organizations where different date formats may lead to confusion, affecting the efficiency of GRC operations like audit trails, compliance reporting, and risk management processes.

**Technical Impact when configured:**

- Determines the date format for displaying and interpreting date data in workflow emails and affected roles grids. 
- Helps in aligning date presentations with user expectations and regional settings, improving ease of use and reducing the risk of date-related errors in workflow processing.

**Example Scenario:**

An organization with operations in both the US (where the MM/dd/yyyy format is common) and Europe (where the dd/MM/yyyy format is prevalent) needs to configure the Workflow Display Date Format to match the regional expectations of their users. By setting the parameter appropriately, Pathlock ensures that all workflow-related communications to users in these regions are clear and unequivocal, thus streamlining GRC processes and enhancing compliance alignment.

**Related Settings:**

- RequestHandled
- CreateNewCultureInfoWithDateFormat

**Best Practices:** 

- Configure when: You are setting up Pathlock for the first time, or when your organization enters new geographical markets with different date format preferences.
- Avoid when: There is no clear consensus on a date format preference within your organization or if such changes could confuse users accustomed to the default format.