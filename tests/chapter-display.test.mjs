import test from 'node:test';import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';
const app=await readFile(new URL('../app.js',import.meta.url),'utf8');
test('Kapitelanzeige berechnet Aufgabenanzahl aus den Daten',()=>{
 assert.match(app,/chapterTasks\(ch\.id\)\.length/);
 assert.doesNotMatch(app,/8 Aufgaben pro Kapitel/);
});
test('Symbol-Drops, lokaler Diagrammvergleich und Legende sind integriert, kein Upload',()=>{
 assert.match(app,/data-symbol-drop/);assert.match(app,/data-slot-answer/);assert.match(app,/drawio-steps/);assert.match(app,/draw.io-Vorlage herunterladen/);assert.match(app,/renderLegend/);
 assert.doesNotMatch(app,/data-upload|input type=\"file\"|awaitImageUpload|data-remove-image/);
});

test('Neue UE-3-Symbole und interaktive Parallel-/Schleifenlogik sind vorhanden',()=>{
 assert.match(app,/if\(k==='and'\)/);
 assert.match(app,/data-parallel/);
 assert.match(app,/data-compare/);
 assert.match(app,/loop-slider/);
 assert.match(app,/Aus UE 2/);
});
