# Platform capabilities

Last checked: 2026-07-17

This page records the platform facts that shape TUEL AI blueprints. It is not a promise that a connection is enabled for any owner. Features, plan access, and permissions can change, so check the linked official page before relying on a capability.

## Claude Cowork

- Cowork requires an eligible paid Claude plan. Tasks run on Anthropic infrastructure, while local file and browser work requires Claude Desktop to remain open.
- Cowork sessions and files are saved to the owner's Claude account. The original working folder remains under the owner's control, but files selected for a task are processed by Claude. A blueprint must never promise "no upload" or "never leaves this computer."
- Cowork offers Manual, Auto, and Skip permission modes. TUEL recommends Manual for setup, new connections, sensitive sources, and anything with write capability. Auto is appropriate only for reviewed action-level A or B work. TUEL blueprints never recommend Skip.
- Folder instructions and project instructions can help behavior persist between chats. They do not turn a folder into a plugin, Skill package, installed agent, or imported schedule.

Official sources:

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Organize tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

## Scheduled work

Schedule files in a blueprint are copy-and-paste recipes. They are not imported automatically. If the scheduling screen offers a folder field, choose the business folder. A task that needs local files requires Claude Desktop and the folder to be available. If those conditions are not met, run the prompt manually. A recipe must report missing or stale input and must never guess, overwrite a previous run, or perform an external action.

## Connections

Actual tool capability and permitted blueprint behavior are separate:

- Gmail can search and read mail, create drafts, and manage some mailbox content. It cannot send mail through the Google Workspace connection. TUEL still treats every draft and mailbox change as owner-reviewed work.
- The official Square connection is described as read and write. TUEL uses it read-only unless an exact reversible draft action is approved in an owner-present session.
- Other tools may vary by plan, region, provider, and current connection. Every blueprint includes a paste-or-export fallback.

Official sources:

- [Use Google Workspace connections](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Square connection](https://claude.com/connectors/square)
- [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

## Review rule

Recheck this record before changing public capability claims, permission guidance, scheduling instructions, or connection metadata. Record the new check date in each changed manifest.
