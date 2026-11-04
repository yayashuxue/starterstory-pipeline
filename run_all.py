#!/usr/bin/env python3
"""
Run all steps of the pipeline in sequence
"""
import subprocess
import sys

def run_step(step_num, script_name, description):
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {description}")
    print('='*60)
    
    result = subprocess.run(["python3", script_name])
    
    if result.returncode != 0:
        print(f"\n✗ Step {step_num} failed!")
        return False
    
    print(f"\n✓ Step {step_num} complete!")
    return True

def main():
    print("Starter Story Analysis Pipeline")
    print("="*60)
    
    steps = [
        (1, "step1_get_video_urls.py", "Getting video URLs"),
        (2, "step2_get_transcripts.py", "Downloading transcripts"),
        (3, "step3_analyze_chapters.py", "Analyzing chapters"),
        (4, "step4_summarize_and_refine.py", "Summarizing and refining"),
        (5, "step5_extract_patterns.py", "Extracting cross-video patterns"),
    ]
    
    for step_num, script, desc in steps:
        if not run_step(step_num, script, desc):
            sys.exit(1)
    
    print(f"\n{'='*60}")
    print("🎉 PIPELINE COMPLETE!")
    print('='*60)
    print("\nOutput files:")
    print("  - video_urls.json (video metadata)")
    print("  - transcripts/ (raw transcripts)")
    print("  - chapters_analysis.csv (chapter excerpts)")
    print("  - chapters_analysis_refined.csv (per-video summaries)")
    print("  - patterns_analysis.json (cross-video patterns)")

if __name__ == "__main__":
    main()
