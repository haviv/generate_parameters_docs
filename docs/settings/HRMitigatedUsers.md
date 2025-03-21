# HR Mitigated Users

**Technical Name:** HRMitigatedUsers

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter controls which users are in the learning phase within the Pathlock GRC platform. It's specifically used to manage a list of SAP user names that are considered to be in a learning or observation period for their transactions.

**Business Impact:**

Understanding and setting the HR Mitigated Users parameter accurately is vital for maintaining proper security and compliance posture. It allows businesses to monitor and mitigate risks associated with newly onboarded users or users in transitional roles by tracking their transaction behaviors in a controlled environment.

**Technical Impact when configured:**

When this parameter is configured, the system will include specified users in a learning phase, where their transactions and activities can be monitored without immediately affecting their access rights. This is crucial for gradually integrating users into sensitive roles while ensuring compliance and minimizing potential security threats.

**Examples Scenario:**

A company is integrating a new finance team member who will have access to critical SAP financial transactions. To ensure compliance and minimize risk, the company adds this new user to the HR Mitigated Users list. This action allows the company to monitor the user's transaction activities closely during the learning phase before granting full transaction privileges.

**Related Settings:** 

- TAAllowedTransactions
- SapSysUser

**Best Practices:** 

- **configure when:** New users are onboarded into roles that require sensitive access, or when existing users are transitioning into new roles that necessitate a period of observation.
  
- **avoid when:** Users are fully trained and trusted, or for roles that do not interact with sensitive transactions where monitoring is deemed unnecessary.