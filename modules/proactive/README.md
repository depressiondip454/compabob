# Module: Proactive

Runs the assistant on a schedule. Two tasks ship with it: a **morning brief** and a **weekly review**. Each runs headless, writes its output to `reports/proactive/`, and logs whether it succeeded. Nothing is sent anywhere; you read the output when you want it.

## How it works

- `run-task.sh <task>` invokes the assistant headless (`claude -p`) on the prompt in `tasks/<task>.txt`, with the kit as its working directory, and saves the result to `reports/proactive/<task>-<date>.md`.
- `install.sh` generates schedule files (a launchd plist on macOS, a cron line on Linux) so the tasks run automatically. It does not touch your system scheduler on its own: it generates the files and tells you the one command to activate them.

## Cost note

Each scheduled run is a headless `claude -p` call. It runs on your Claude subscription or API credits like any other session. The runner pins `--model sonnet` to keep this modest. Two runs a day (one brief, one weekly) is light. If you add more tasks, keep the cost in mind.

## Enable it

```bash
cd modules/proactive
bash install.sh
```

`install.sh` will:

1. Detect your OS.
2. Generate the schedule files into `modules/proactive/generated/`.
3. Print the exact command to activate them.

Then set `proactive: true` in `config/user.config.yaml`.

To test a task immediately, without waiting for the schedule:

```bash
bash modules/proactive/run-task.sh morning-brief
cat reports/proactive/morning-brief-$(date +%Y-%m-%d).md
```

## Add a task

Drop a new prompt file in `tasks/<name>.txt`, then add a schedule entry in `install.sh`. The prompt should be self-contained: it runs in a fresh headless session with no conversation history.

## Disable it

Remove the schedule (the deactivation command is printed by `install.sh`), and set `proactive: false` in `config/user.config.yaml`.
