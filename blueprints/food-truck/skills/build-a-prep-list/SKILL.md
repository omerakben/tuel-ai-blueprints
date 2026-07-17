# Build a prep list

Turns tomorrow's plan into one page for the kitchen: what to batch tonight, what to buy in the morning, what to load on the truck.

## When to run this

The evening before a service, once you know tomorrow's spot and roughly what kind of day it will be. It pairs well with the end-of-day close: numbers first, prep list while the day is still fresh in your head.

## What Claude reads first

- business/services.md — the menu, so the list is built item by item.
- business/suppliers.md — your par levels and restock points, where you've set them.
- templates/prep-list.md — the shape the list takes.
- Today's daily close in reports/, if there is one — what sold out and what came home matters for tomorrow.

From you: tomorrow's plan. The spot and hours, what kind of crowd you expect, and any event or special. Plus rough counts of what's already prepped or on the truck, in any shape — "two trays of the sauce, half a case of buns" is plenty.

## Steps

1. Ask for tomorrow's plan if it hasn't come up. No plan, no list — Claude never sizes a prep list off a guess about where you'll be or how busy it gets.
2. Walk the menu. For each item you'll serve tomorrow, Claude works out what needs batching from what you said is already made, and asks where it's unsure. Your expected crowd sets the size; if you didn't give one, Claude asks for your gut number instead of inventing one.
3. Sort every need into the three piles from templates/prep-list.md: batch tonight, buy in the morning, load the truck.
4. Check the buy pile against business/suppliers.md. Anything that also sits below its restock point gets a note, so a morning shop and a proper restock don't get confused.
5. Anything Claude couldn't place — an item with no par level, a count you didn't give — goes in a questions list at the top, never silently guessed.
6. Show you the draft. You move items, change amounts, cross things off. When it looks right, Claude saves it.

## What you get

One page in reports/, named like reports/prep-list-YYYY-MM-DD.md, dated for the service day it covers:

- Batch tonight: item, amount, and what it's for.
- Buy in the morning: item and amount — buying is yours; this is a shopping list, not an order.
- Load the truck: everything that has to make it on board, worth reading twice at dawn.
- Questions for you, at the top, so nothing hides.

## Never

- Never guess a quantity, a crowd size, or what's already prepped. Missing numbers become questions.
- Never turn the buy list into a supplier order or send it anywhere. Buying and ordering are the owner's, every time.
- Never make the call on food safety — how long something keeps, what can be held overnight, what temperature anything needs. Claude repeats what the owner wrote down, and otherwise says "your call".
- Never size a list off an unconfirmed spot. If tomorrow's plan is up in the air, the list waits or covers only what's true either way.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
