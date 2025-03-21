# Mail Listener Decline Keywords

**Technical Name:** MailListnerDeclineKeywords

**Category:** Workflow

**Default Value:** (Information not available)

**Impact Level:** Medium

**Description:**

This parameter specifies the keywords or phrases used to automatically decline workflow requests when detected in the subject or body of emails processed by the Mail Listener feature in Pathlock's Cloud GRC platform. It is a crucial component for automating workflow request management and ensuring timely action on relevant requests.

**Business Impact:**

Automating the decline of workflow requests based on specific keywords can significantly reduce manual efforts and streamline operations. It ensures that irrelevant or unauthorized requests are filtered out early in the process, allowing teams to focus on valid and essential requests. This efficiency can directly impact overall security posture and compliance by ensuring that only appropriate actions are taken on workflow requests.

**Technical Impact when configured:**

Upon configuration, any incoming email that the Mail Listener processes will be scanned for the specified decline keywords. If any of these keywords are found, the associated workflow request will be automatically declined. This helps in reducing the volume of requests that need manual review and prevents unauthorized or irrelevant workflow actions from being executed.

**Examples Scenario:**

Scenario: An organization wants to automatically decline all workflow requests related to "System Shutdown" during business hours. By adding "System Shutdown" as a decline keyword, the Mail Listener will automatically decline all such requests, ensuring that no accidental or unauthorized shutdowns are initiated during critical business hours.

**Related Settings:**

- MailListenerMailProtocol

**Best Practices:** Configure when, avoid when

- **Configure when** you want to automate the decline of specific types of workflow requests that are known to be irrelevant, unauthorized, or potentially harmful. This is particularly useful in managing high-volume environments where manual review of every request is not feasible.
- **Avoid when** there is a high likelihood of false positives that could inadvertently decline valid workflow requests. In such cases, it is better to use a more nuanced approach or to enhance the keyword list regularly based on review of declined requests.