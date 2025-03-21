# User Open Request Screen Show End Request Confirm Message

**Technical Name:** UserOpenRequestScreenShowEndRequestConfirmMessage

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This setting controls whether a confirmation message is displayed to the user when they attempt to end a request from the open request screen. Enabling this feature ensures that users are prompted to confirm their action before the request is officially closed, preventing accidental terminations of requests.

**Business Impact:**

The presence of a confirmation message can significantly reduce the likelihood of users inadvertently ending important requests, thus safeguarding the integrity of the workflow process. This feature is particularly valuable in environments where requests undergo multiple levels of approval and any premature termination can lead to compliance issues or security risks.

**Technical Impact when configured:**

When enabled, this setting introduces an additional step in the request termination process, requiring users to acknowledge their intention to end a request. This could slightly extend the time it takes to close a request but enhances process control and accuracy in handling requests.

**Examples Scenario:**

An employee initiates a request for access to sensitive financial documents. Upon realizing they selected the wrong documents, they attempt to end the request. With the confirmation message feature enabled, they are prompted to confirm their decision, ensuring that the action is intentional and preventing accidental termination of the request.

**Related Settings:**

- UserOpenRequestScreenShowAddInfoButton

**Best Practices:** Configure when multiple levels of request approval are required or when working with sensitive or critical requests to prevent accidental termination. Avoid when speed is prioritized over process integrity and the risk of accidental termination is deemed minimal.