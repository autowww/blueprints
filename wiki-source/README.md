# GitHub Wiki mirror

The wiki at [github.com/autowww/blueprints/wiki](https://github.com/autowww/blueprints/wiki) is filled by **`sync-wiki.sh`**, which copies almost all `*.md` from this repo into the wiki (same folder layout), rewrites links to `.html` handbook files to point at the **code** tab on GitHub, and regenerates **`_Sidebar.md`**.

## One-time setup

1. Repo **Wiki** tab → **Create the first page**.
2. Page name **`Home`** → save (content can be a stub; the script will replace it on first sync).

Until step 2 is done, `git clone https://github.com/autowww/blueprints.wiki.git` fails with “repository not found.”

## Each time you want to refresh the wiki

```bash
cd /path/to/blueprints   # clone of autowww/blueprints, main up to date
./wiki-source/sync-wiki.sh
```

Requirements: `git`, `python3`, and credentials that can **push** to `https://github.com/autowww/blueprints.wiki.git` (same GitHub account / token as for the main repo).

## What gets mirrored

- All `*.md` under `sdlc/`, `docs/`, and `agents/`, except:
  - anything under **`wiki-source/`**
  - files named **`*.template.md`**

## What does *not* get mirrored

- **HTML handbook** (`sdlc/docs/*.html`) — GitHub Wiki is Markdown-oriented; those stay in the main repo. Synced Markdown links to `.html` are rewritten to `github.com/.../blob/main/sdlc/docs/...`.
- **Shell scripts, SVG, Dockerfiles**, etc. — still only in the code repo.

## Legacy script

`publish-wiki.sh` only copied `Home.md` and `_Sidebar.md` (no full docs). Use **`sync-wiki.sh`** instead.
