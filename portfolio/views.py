from django.shortcuts import render
from django.http import Http404


def deck_images(folder, page_count, captions):
    """Build image metadata for rendered design-deck pages."""
    return [
        {
            "src": f"img/projects/{folder}/page-{index}.webp",
            "alt": captions[index - 1],
            "caption": captions[index - 1],
        }
        for index in range(1, page_count + 1)
    ]


PROJECTS = {
    "games": {
        "title": "Game Projects",
        "description": (
            "This section presents my game projects with playable prototypes, mechanics, "
            "level-design notes, code logic, and visual design decks."
        ),
        "projects": [
            {
                "name": "Missile Command",
                "slug": "missile-command",
                "description": (
                    "A C++ and OpenGL arcade-defense remake focused on turret control, "
                    "missile interception, and collision detection."
                ),
                "tech": "C++ / OpenGL / AABB Collision / Game Loop",
                "github": "https://github.com/1261082413/Missile-Command-game",
                "demo_slug": "missile-command",
                "detail": (
                    "I re-implemented the classic Missile Command idea and built a simplified "
                    "browser demo for this portfolio. The project helped me practise input mapping, "
                    "game-loop structure, collision detection, object spawning, and real-time rendering."
                ),
                "design": {
                    "subtitle": "Arcade remake with clear player input, collision logic, and game-loop thinking.",
                    "role": "Solo developer / gameplay programmer",
                    "type": "Arcade defense game",
                    "focus": [
                        "Turret selection",
                        "Mouse-to-world input",
                        "AABB collision",
                        "Object update loop",
                    ],
                    "pillars": [
                        {
                            "title": "Readable core loop",
                            "body": "Enemy missiles fall toward the cities. The player selects a turret, fires toward the target, and tries to protect the city line.",
                        },
                        {
                            "title": "Input as a command",
                            "body": "Mouse position is converted into world space, then the selected turret creates a new outgoing missile command.",
                        },
                        {
                            "title": "Simple collision model",
                            "body": "I used AABB-style checks to keep the collision system fast and easy to debug for missiles, cities, and destroyed objects.",
                        },
                    ],
                    "sections": [
                        {
                            "title": "Gameplay design",
                            "paragraphs": [
                                "The game asks players to protect cities from incoming missiles. Turrets are placed at the bottom of the screen, while enemy missiles approach from above.",
                                "My version adds an explicit turret-selection step: the player uses keyboard input to choose the controlled turret, then clicks the mouse in the target direction. This makes each shot feel more intentional than a single-click interaction.",
                            ],
                        },
                        {
                            "title": "Technical design",
                            "paragraphs": [
                                "The mouse input is captured in screen space, converted into world space, and passed to a fireMissile function. That function behaves like a command: it validates the selected silo, calculates direction and velocity, then pushes a new missile into the active queue.",
                                "The world update loop refreshes object states, checks collisions, removes destroyed items, and renders the frame. This separates input, simulation, and rendering into clear steps.",
                            ],
                        },
                        {
                            "title": "What interviewers can see",
                            "points": [
                                "I understand how to translate player input into gameplay actions.",
                                "I can explain why a simple collision algorithm is appropriate for a small real-time game.",
                                "I can break a game into update, collision, removal, and rendering stages.",
                            ],
                        },
                    ],
                    "deck": {
                        "pdf": "docs/MissileCommand.pdf",
                        "label": "Missile Command design deck",
                        "images": deck_images(
                            "missile",
                            3,
                            [
                                "Project overview and C++/OpenGL remake goal",
                                "Gameplay rules, turret control, and AABB collision note",
                                "Input conversion, fireMissile command, and world-update logic",
                            ],
                        ),
                    },
                    "takeaways": [
                        "Designed a complete arcade gameplay loop from input to rendering.",
                        "Connected control decisions with code-level implementation.",
                        "Used a simple collision approach that fits the project's scale.",
                    ],
                },
            },
            {
                "name": "Blade and Bow",
                "slug": "platform-game",
                "description": (
                    "A 2D platform combat game built around blade combos, strategic bow attacks, "
                    "enemy pressure, and trap-based level design."
                ),
                "tech": "Unity / C# / Animator State Machine / Level Design",
                "github": "https://github.com/1261082413/Platform-game",
                "detail": (
                    "This project focuses on platform-game mechanics and combat pacing. I designed "
                    "the player around two attack modes, then used enemies, traps, item placement, "
                    "and vertical map structure to create a stronger balance between fighting and movement."
                ),
                "design": {
                    "subtitle": "A platformer where combat choices, enemy pressure, and traps shape the player's route.",
                    "role": "Game designer / Unity programmer",
                    "type": "2D platform combat game",
                    "focus": [
                        "Three-stage combo",
                        "Bow timing balance",
                        "Enemy attack windows",
                        "Trap and item pacing",
                    ],
                    "pillars": [
                        {
                            "title": "Combat first",
                            "body": "The blade combo is designed as the main combat expression, while platforming and traps add pressure around it.",
                        },
                        {
                            "title": "Risk and reward",
                            "body": "Later combo stages deal more damage, but players must judge enemy timing instead of repeating the first attack.",
                        },
                        {
                            "title": "Strategic ranged option",
                            "body": "The bow fires horizontally with strong impact, but its longer wind-up prevents it from becoming a safe spam option.",
                        },
                    ],
                    "sections": [
                        {
                            "title": "Core concept",
                            "paragraphs": [
                                "The game takes place in a medieval-fantasy world. The player defeats enemies with a blade and bow while navigating traps and platforming challenges.",
                                "The main objective is not only to reach the end of a level, but to make decisions under pressure: when to fight, when to dodge, when to use range, and when to move quickly through hazards.",
                            ],
                        },
                        {
                            "title": "Player attack design",
                            "paragraphs": [
                                "The blade uses a three-stage combo. I slowed the first attack to avoid repetitive button-spamming, then made the second and third attacks stronger so the full combo has real value.",
                                "The final attack includes knockback, which prevents enemies from being locked in place and keeps close combat more dynamic.",
                                "The bow shoots horizontally without drop-off. This supports parkour situations where melee combat would be risky, but the longer wind-up and map layout prevent players from safely clearing every challenge from a distance.",
                            ],
                        },
                        {
                            "title": "Enemy, trap, and item design",
                            "paragraphs": [
                                "The knight enemy has a longer attack wind-up so players have time to react. Its hitbox focuses lower on the body, making jumping a valid dodge choice.",
                                "Flying enemies use fixed waypoint movement and act more like moving obstacles in high-pressure levels.",
                                "Traps include moving gears, swinging gears, disappearing platforms, and spikes. Coins and health packs motivate exploration, but their placement can also pull players toward risky areas.",
                            ],
                        },
                        {
                            "title": "Code and system logic",
                            "points": [
                                "Animator State Machine controls player states such as ground, air, attack, bow, hit, and death.",
                                "PlayerController handles running, jumping, melee attacks, ranged attacks, and hit response.",
                                "FlyingController uses waypoint movement to create predictable but dangerous enemy routes.",
                                "Health and Damage components separate damage calculation from character movement logic.",
                            ],
                        },
                    ],
                    "deck": {
                        "pdf": "docs/BladeAndBow.pdf",
                        "label": "Blade and Bow design deck",
                        "images": deck_images(
                            "platform",
                            4,
                            [
                                "Game identity: 2D roguelike-inspired platform combat",
                                "Overview and two-mode character attack design",
                                "Level mechanics: unstable slabs, flying enemy, coins, and health packs",
                                "Code logic: animator state machine, controllers, health and damage components",
                            ],
                        ),
                    },
                    "takeaways": [
                        "Balanced melee and ranged attacks through timing, damage, and map design.",
                        "Used enemy behavior and traps to create pressure rather than random difficulty.",
                        "Separated gameplay systems into controller, state-machine, health, and damage logic.",
                    ],
                },
            },
            {
                "name": "Shattered Shadows",
                "slug": "shooting-game",
                "description": (
                    "A 2D pixel-style shooting game with weapon progression, rolling dodge, "
                    "AI patrols, destructible objects, and staged level progression."
                ),
                "tech": "Unity / C# / NavMesh / Pixel Art / Roguelike Systems",
                "github": "https://github.com/1261082413/RougeLike-shooting-game",
                "detail": (
                    "This project explores shooting mechanics, weapon variety, enemy AI, level pacing, "
                    "and a small narrative framework. I designed the game to combine satisfying combat "
                    "with readable progression through hub, tutorial, and combat-heavy spaces."
                ),
                "design": {
                    "subtitle": "A pixel shooting project showing weapon systems, dodge mechanics, AI behavior, and level pacing.",
                    "role": "Game designer / Unity programmer",
                    "type": "2D pixel-style shooting game",
                    "focus": [
                        "Weapon system",
                        "Rolling dodge",
                        "NavMesh enemy AI",
                        "Destructible props",
                        "Difficulty curve",
                    ],
                    "pillars": [
                        {
                            "title": "Weapon-driven combat",
                            "body": "Players can buy and upgrade different weapons, each with different firing behavior and tactical use.",
                        },
                        {
                            "title": "Readable level curve",
                            "body": "The game moves from a hub area to a first-battle tutorial and then into a more demanding school-building level.",
                        },
                        {
                            "title": "Interactive environment",
                            "body": "Crates and tables can be destroyed, adding item drops and moment-to-moment choices during combat.",
                        },
                    ],
                    "sections": [
                        {
                            "title": "Core concept",
                            "paragraphs": [
                                "Shattered Shadows is a 2D pixel-style shooting game that combines roguelike elements with a distinctive weapon system.",
                                "The objective is to defeat enemies, survive each level, collect coins, and become stronger through shop purchases and weapon progression.",
                            ],
                        },
                        {
                            "title": "Level progression",
                            "paragraphs": [
                                "The Police Office works as a hub area where the player learns the background and can buy weapons or health items.",
                                "City Street introduces the first battle and teaches attacking, bullet dodging, and destroying objects to obtain items.",
                                "School Buildings increases pressure with more enemies, obstacles that limit dodging, and destructible objects that can drop health packs so the difficulty feels intense but still manageable.",
                            ],
                        },
                        {
                            "title": "Character and AI design",
                            "paragraphs": [
                                "The player primarily attacks by shooting and uses rolling to dodge incoming bullets. I separated the player's body and hands so weapon changes from the shop can be implemented more flexibly.",
                                "Enemies use a NavMesh-based patrol and chase setup. When the player enters attack range, enemies begin chasing and shooting, which creates a clear combat trigger.",
                            ],
                        },
                        {
                            "title": "Item and environment design",
                            "paragraphs": [
                                "Environmental objects create small tactical decisions. Crates always drop a health pack, while tables only have a chance to drop one. Destroyed objects also generate random wood splinters for feedback.",
                                "This gives the player a reason to interact with the environment during combat instead of treating rooms as static backgrounds.",
                            ],
                        },
                    ],
                    "deck": {
                        "pdf": "docs/ShatteredShadows.pdf",
                        "label": "Shattered Shadows design deck",
                        "images": deck_images(
                            "shooting",
                            5,
                            [
                                "Game title screen, GitHub QR, and Unity project identity",
                                "Overview: pixel shooting game, roguelike structure, and narrative goal",
                                "Weapon system and upgrade decisions",
                                "Level environments: Police Office, City Street, and School Buildings",
                                "Level design detail with route planning, combat zones, shop, and next-level gates",
                            ],
                        ),
                    },
                    "takeaways": [
                        "Designed a difficulty curve from hub to tutorial to full combat level.",
                        "Connected weapon variety, rolling dodge, and enemy AI into one combat loop.",
                        "Used destructible props and item drops to make the environment part of gameplay.",
                    ],
                },
            },
        ],
    },
    "modeling": {
        "title": "3D Modelling Projects",
        "description": "This section presents my 3D modelling and digital design work with research, procedural modelling, and rendering notes.",
        "projects": [
            {
                "name": "Moon Guitar",
                "slug": "moonguitar",
                "description": (
                    "A programmable 3D modelling project inspired by the traditional Chinese Yueqin, "
                    "built with procedural geometry and rendered with separated materials."
                ),
                "tech": "JavaScript / OpenSCAD / STL / Three.js Materials",
                "github": "https://github.com/1261082413/MoonGuitar-project",
                "detail": (
                    "In this project, I used code-driven modelling to recreate the Moon Guitar. "
                    "I researched the instrument's visible structure, generated major parts with "
                    "programmable geometry, exported the model to STL, and experimented with material "
                    "settings to make different surfaces feel distinct."
                ),
                "design": {
                    "subtitle": "A procedural modelling project that turns reference research into structured 3D geometry.",
                    "role": "3D modelling programmer / visual designer",
                    "type": "Procedural 3D model",
                    "focus": [
                        "Reference research",
                        "Parametric modelling",
                        "STL export",
                        "Material separation",
                        "Rendering",
                    ],
                    "pillars": [
                        {
                            "title": "Research before modelling",
                            "body": "I first studied reference images to identify the main visible parts: circular soundboard, bridges, neck, strings, and sound holes.",
                        },
                        {
                            "title": "Code-generated form",
                            "body": "Instead of modelling only by hand, I used programmable geometry so dimensions and repeated structures could be controlled in code.",
                        },
                        {
                            "title": "Material storytelling",
                            "body": "The final model is split into multiple parts so each section can use a different material response during rendering.",
                        },
                    ],
                    "sections": [
                        {
                            "title": "Concept and research",
                            "paragraphs": [
                                "Moon Guitar is based on the traditional Chinese Yueqin, which has a round body and short slender neck. The project goal was to capture the instrument's recognizable silhouette and translate it into a digital model.",
                                "During reference research, I observed that the soundboard is built around a circular disc and one or two bridge structures. I created these pieces separately, joined them, and added sound holes to the main body.",
                            ],
                        },
                        {
                            "title": "Procedural modelling approach",
                            "paragraphs": [
                                "I used OpenSCAD-style programmable modelling to define parameters such as scale, radius, thickness, bridge radius, and bridge height.",
                                "This method made the model easier to revise because important dimensions are controlled by variables instead of only manual edits.",
                            ],
                        },
                        {
                            "title": "Export and rendering",
                            "paragraphs": [
                                "After generating the geometry, I exported the model to STL format. For rendering, I divided the model into six parts and assigned unique material settings to different areas.",
                                "The material work includes properties such as metalness, roughness, transparency, transmission, and clearcoat to create a more polished visual result.",
                            ],
                        },
                    ],
                    "deck": {
                        "pdf": "docs/MoonGuitar.pdf",
                        "label": "Moon Guitar design deck",
                        "images": deck_images(
                            "moon",
                            4,
                            [
                                "Instrument background and final model preview",
                                "OpenSCAD introduction and programmable bridge-generation code",
                                "Reference research and early structural model",
                                "STL export and material/rendering settings",
                            ],
                        ),
                    },
                    "takeaways": [
                        "Translated visual references into a programmable 3D modelling plan.",
                        "Used parameters to control geometry and support iteration.",
                        "Separated model parts to improve material and rendering control.",
                    ],
                },
            },
        ],
    },
    "school": {
        "title": "School Projects",
        "description": "This section presents academic projects completed during my Computer Science studies.",
        "projects": [
            {
                "name": "CW5 Logistics App",
                "slug": "logistics",
                "description": "A Django-based logistics management system with customer tracking and admin management features.",
                "tech": "Django / Python / Bootstrap / SQLite",
                "github": "https://github.com/1261082413/cw5-logistics-app",
                "detail": "This project is a web application for logistics management. It includes customer functions, tracking information, and admin management features. Through this project, I practised Django development, URL routing, templates, user interface design, and database interaction.",
            },
            {
                "name": "CISC327 Group Project",
                "slug": "cisc327",
                "description": "A software engineering group project involving system design, implementation, and testing.",
                "tech": "Python / Flask / Software Engineering / Testing",
                "github": "https://github.com/nid2001/CISC327_Group36-CH",
                "detail": "This group project involved software design, implementation, testing, and teamwork. It helped me understand the software development process, including requirements, system structure, coding, and test coverage.",
            },
            {
                "name": "Emoji Passport",
                "slug": "emoji-passport",
                "description": "A human-centred security prototype comparing emoji passwords and text passwords.",
                "tech": "Django / HCI / Human-Centred Security",
                "github": "https://github.com/1261082413/Emoji-passport-test",
                "detail": "This project is a human-centred security prototype. It compares emoji-based passwords with traditional text passwords. The project focuses on usability, memorability, user experience, and authentication design.",
            },
        ],
    },
}


DEMOS = {
    "missile-command": {
        "title": "Missile Command Demo",
        "subtitle": "A simplified browser version of the missile defense game concept.",
        "script": "js/demos/missile_demo.js",
        "controls": [
            "Click on incoming missiles to intercept them.",
            "Protect the cities at the bottom of the screen.",
            "Press Restart Demo to play again.",
        ],
    },
}


def home(request):
    categories = [
        {
            "name": "Game Projects",
            "slug": "games",
            "description": "Missile Command, Blade and Bow, and Shattered Shadows with design breakdowns",
        },
        {
            "name": "3D Modelling Projects",
            "slug": "modeling",
            "description": "Moon Guitar procedural modelling and rendering process",
        },
        {
            "name": "School Projects",
            "slug": "school",
            "description": "Logistics App, CISC327 Project, and Emoji Passport",
        },
    ]

    return render(request, "portfolio/home.html", {"categories": categories})


def category(request, category_name):
    category_data = PROJECTS.get(category_name)

    if category_data is None:
        raise Http404("Category not found")

    return render(request, "portfolio/category.html", {"category": category_data})


def project_detail(request, project_name):
    selected_project = None

    for category in PROJECTS.values():
        for project in category["projects"]:
            if project["slug"] == project_name:
                selected_project = project
                break
        if selected_project is not None:
            break

    if selected_project is None:
        raise Http404("Project not found")

    return render(request, "portfolio/project_detail.html", {"project": selected_project})


def game_demo(request, demo_slug):
    demo = DEMOS.get(demo_slug)

    if demo is None:
        raise Http404("Demo not found")

    return render(request, "portfolio/game_demo.html", {"demo": demo})
