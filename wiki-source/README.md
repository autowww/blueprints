# GitHub Wiki source

These Markdown files are meant to be published to **[github.com/autowww/blueprints/wiki](https://github.com/autowww/blueprints/wiki)**.

GitHub does **not** create the wiki Git remote until the **first page** exists.

## One-time: create the wiki

1. Open the repo **Wiki** tab → **Create the first page**.
2. Set the page name to **`Home`** (capital **H** — this becomes the default landing page).
3. Paste the contents of **`Home.md`** from this folder (or a one-line stub like `# Blueprints`, then Save).
4. Save the page.

## Publish updates from this repo

From a clone of **`autowww/blueprints`** with GitHub auth configured:

```bash
./wiki-source/publish-wiki.sh
```

Or manually:

```bash
git clone https://github.com/autowww/blueprints.wiki.git
cp /path/to/blueprints/wiki-source/Home.md blueprints.wiki/
cp /path/to/blueprints/wiki-source/_Sidebar.md blueprints.wiki/
cd blueprints.wiki && git add Home.md _Sidebar.md && git commit -m "Sync wiki" && git push
```

The wiki remote may use branch **`master`** or **`main`** depending on when the wiki was created; the script tries both.
