# Change Documents Show Change Type Column

**Technical Name:** ChangeDocumentsShowChangeTypeColumn

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ChangeDocumentsShowChangeTypeColumn` parameter controls the visibility of the 'Change Type' column in the change document reports within the Pathlock Cloud GRC platform. When enabled, this setting allows users to see the type of change (e.g., addition, update, deletion) that was made in the document, providing deeper insights into the modifications history.

**Business Impact:**

Enabling this feature helps organizations to more effectively monitor and audit changes within their GRC data landscape. It enhances transparency and accountability by making it clear what kind of changes were made, thereby supporting compliance with internal policies and external regulations.

**Technical Impact when configured:**

Once configured, reports generated from the `ChangeDocumentService` will include an additional column, 'Change Type', which can be critical for audits or internal reviews to understand the nature of changes made to documents within the system. This setting may influence the readability of the reports and the speed at which users can comprehend the documented changes.

**Examples Scenario:**

A compliance officer needs to verify that all changes to sensitive documents in the last quarter were authorized and correctly categorized. By enabling the `ChangeDocumentsShowChangeTypeColumn`, the officer can quickly generate a report from Pathlock GRC's change document service and see at a glance the type of changes made, facilitating a more efficient audit process.

**Related Settings:** 

- RoleDescriptionMaxLengthForDisplay

**Best Practices:** configure when audits and compliance checks require detailed change logs; avoid when simplicity in report viewing is preferred.