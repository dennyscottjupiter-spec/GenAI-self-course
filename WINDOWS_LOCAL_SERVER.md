# How to Find and Stop a Python Server on Windows (Port 8000)

## The Quick Way

**If you remember which terminal started it:**
```
Ctrl + C
```
Press these keys in the terminal where the server is running. Done.

---

## The Full Way (If You Forgot the Terminal)

### Step 1: Find the Process ID (PID)

Open **PowerShell** (not Command Prompt) and run:

```powershell
netstat -ano | Select-String :8000
```

You'll see output like:
```
  TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       16088
  TCP    [::]:8000              [::]:0                 LISTENING       16088
```

**Note the number on the right** — that's your PID (in this example: `16088`).

---

### Step 2: Kill It

Still in PowerShell, run:

```powershell
taskkill /PID 16088 /F
```

Replace `16088` with your actual PID from Step 1.

You'll see:
```
ÊXITO: o processo com PID 16088 foi finalizado.
```
(or `SUCCESS` if your Windows is in English)

---

### Step 3: Verify It's Dead

Run the find command again:

```powershell
netstat -ano | Select-String :8000
```

If nothing appears — port 8000 is free. ✅

---

## One-Line Version (Copy-Paste Ready)

If your PID is `16088`:

```powershell
taskkill /PID 16088 /F
```

That's it.

---

## Common PID Values

Every time you start the server, it gets a different PID. Always run Step 1 to find the current one.

---

## Summary Table

| Task | Command |
|---|---|
| **Find what's using port 8000** | `netstat -ano \| Select-String :8000` |
| **Kill it (replace 16088 with your PID)** | `taskkill /PID 16088 /F` |
| **Verify it's gone** | `netstat -ano \| Select-String :8000` (should show nothing) |

---

## Tips

- Always use **PowerShell**, not Command Prompt (it understands pipes `|`)
- The `/F` flag means "force" — it kills immediately without asking
- If `taskkill` says the PID doesn't exist, the server is already dead
- Port 8000 is only dangerous if your machine is on a public network; at home it's safe. But the safest way to start is:

```powershell
python3 -m http.server 8000 --bind 127.0.0.1
```

This makes it invisible to all other devices.
