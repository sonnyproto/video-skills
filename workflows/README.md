# workflows

**How to make a film, step by step, with a pass mark at every step.**

Whole films are in [films/](../films/), single shots in [moves/](../moves/). This folder holds the process: the order of work, what each
step produces, and how you know it is done. Every workflow here came from a film that went wrong first.

## Workflows

| Category | Workflow | In one line |
|---|---|---|
| audio | [voiceover-then-music](audio/voiceover-then-music/WORKFLOW.md) | Lock the voice as one continuous read, then make music sized to the film |
| modeling | [scene-from-references](modeling/scene-from-references/WORKFLOW.md) | Reference images → code model → side-by-side stills until they match → animate |
| porting | [remotion-to-hyperframes](porting/remotion-to-hyperframes/WORKFLOW.md) | Port a Remotion component frame for frame and prove it with SSIM |

## Layout

```
<category>/<name>/
├── WORKFLOW.md     steps, what each produces, the pass mark, the cost, worked examples
├── scripts/        the measuring scripts the pass marks use (optional)
└── templates/      blank documents the workflow fills in (optional)
```

A workflow is tool-agnostic where it can be; when it names a tool (HyperFrames, ElevenLabs), the step says what the tool
is for, so another tool can take its place.

## Keys and paid services

A step that uses a paid API (fal, ElevenLabs, OpenAI, BytePlus Seedance...) names the environment variable it reads
(`FAL_KEY`, `OPENAI_API_KEY`, `BYTEPLUS_API_KEY`) and what the step needs from it, so another service or a manual route
can take its place. Keys come from the environment or a git-ignored `.env`, never from the repo.

## Licence

MIT, like the rest of the repo.
