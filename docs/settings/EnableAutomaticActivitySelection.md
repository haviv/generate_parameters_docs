# Enable Automatic Activity Selection

**Technical Name:** EnableAutomaticActivitySelection

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This setting controls whether activities within a workflow are selected automatically. When enabled, it streamlines workflow processes by automatically moving the workflow to the next step without manual intervention, assuming conditions for progression are met.

**Business Impact:**

Enabling this parameter can significantly improve efficiency in process flows by reducing manual work and decision-making time for users. It can be particularly impactful in environments where rapid decision-making and process execution are critical to business operations.

**Technical Impact when configured:**

When configured, this parameter affects the flow of work by automatically selecting the appropriate next step in a workflow. This can lead to faster completion of tasks and reduced processing times, contributing to overall system and operational efficiency.

**Examples Scenario:**

- In a compliance review process, once a document has been uploaded and initially reviewed, enabling this setting could automatically forward the document to the next review phase without requiring a manual action from the compliance officer.
- During an access review workflow, after an employee’s manager approves their access request, the system can automatically move the request to the IT security team for final approval, streamlining the approval chain.

**Related Settings:**

None provided in code references.

**Best Practices:** configure when workflow processes are well-defined and standard across different instances, avoiding when workflows require significant manual judgment or case-by-case decision making that cannot be standardized or automated effectively.