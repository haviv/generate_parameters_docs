# ApprovedByDelegateAnnotation Parameter Documentation

## Category:
- Application Configuration

## Default Value:
- `""` (An empty string)

## Impact Level:
- Moderate

## Description:
The `ApprovedByDelegateAnnotation` parameter is designed to prepend an annotation or comment to workflow items approved by delegates in the application. This annotation helps in distinguishing between items approved directly by the primary approver and those approved by delegated authority, maintaining an audit trail and clarity in approval processes.

## Business Impact:
The usage of the `ApprovedByDelegateAnnotation` parameter can significantly improve the transparency and traceability of the approval process within the organization's workflow management system. It enables stakeholders to easily identify how a particular decision was made, ensuring that delegated approvals are correctly recorded and recognizable at a glance.

## Technical Impact when configured:
When set, this parameter alters the display of manager comments within the workflow approval process by adding a specific annotation to comments associated with approvals made by delegates. This modification aids in clear documentation and improves the auditability of the process by providing immediate visibility into the approval path taken.

## Example Scenario:
In a case where an approval is required for a financial requisition, and the primary financial officer delegates the approval responsibility to their assistant, any approval made by the assistant will have the `ApprovedByDelegateAnnotation` prefixed to their approval comment. This helps in quickly identifying that the approval was made under delegated authority, providing context for the decision.

## Related Settings:
- `ApprovedByAdminAnnotation`
  
## Best Practices:
- **Configure when**: There is a need to distinguish between direct approvals and delegated approvals, especially in environments where delegation is a common practice.
- **Avoid when**: Your workflow does not involve delegation or if it's unnecessary to distinguish between types of approvals, to keep the process streamlined without extra annotations.

## Context:
The `ApprovedByDelegateAnnotation` parameter is essential in environments where decision delegation is a significant part of the workflow, such as in large organizations with complex approval hierarchies. It plays a critical role in ensuring transparency, accountability, and traceability within the approval process.