**Technical Name:** NotUsedDaysMediumLevel

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used in the reporting context of the Pathlock Cloud GRC platform to identify user accounts that have not been used for a medium level of days. It typically filters or highlights accounts in reports based on their inactivity period that is considered medium by the organization's standards.

**Business Impact:**

Configuring this parameter assists in identifying potentially obsolete or dormant accounts that may no longer require access, thereby tightening security and compliance postures. It helps in risk management by flagging medium risk accounts based on inactivity, which could be a sign of turnover or prolonged absence and might necessitate revocation of access rights or further investigation.

**Technical Impact when configured:**

- Enhances non-active user reports by providing a criterion for filtering user accounts based on a medium level of inactivity.
- Assists in audit and compliance efforts by easily identifying accounts that have not been used for a medium duration, which may contravene certain access policies or standards.

**Example Scenario:**

An organization wants to routinely review user accounts to enforce a clean-up of accounts that haven't been used for a certain period, classified by risk levels (Low, Medium, High). By using the "NotUsedDaysMediumLevel" parameter, the organization can specifically target and review accounts falling into the medium risk category based on inactivity days defined by their policy, thus efficiently managing user account lifecycles and maintaining a minimal access principle.

**Related Settings:** 

- `NotifyUserDeclined`: This setting may be relevant in scenarios where users whose accounts have been identified as inactive (based on the "NotUsedDaysMediumLevel" criteria) are notified when access removal requests are declined.
- `NotifyUserReceived`: Similarly, this setting could be pertinent in informing users when a request related to their inactivity status is submitted, fostering transparent communication.

**Best Practices:** 

- **Configure when:** Regular account review cycles are established, and there is a need to differentiate inactive accounts by risk levels to streamline access review and revocation processes.
- **Avoid when:** The organization does not differentiate inactive accounts by risk levels or when such differentiation does not align with the organization’s access control policies and procedures.